from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAGE_MAP = {
    "index.html": "/",
    "how-we-help.html": "/how-we-help/",
    "our-offerings.html": "/our-offerings/",
    "free-fit-check.html": "/free-fit-check/",
    "intelligence-lab.html": "/intelligence-lab/",
    "insights.html": "/insights/",
    "about.html": "/about/",
    "privacy-policy.html": "/privacy-policy/",
    "analytics-health-check.html": "/analytics-health-check/",
    "decision-system-reset.html": "/decision-system-reset/",
    "fractional-analytics.html": "/fractional-analytics/",
    "dashboard-trust-scorecard.html": "/dashboard-trust-scorecard/",
    "dashboard-trust-scorecard-download.html": "/dashboard-trust-scorecard-download/",
    "thank-you.html": "/thank-you/",
    "scorecard-thank-you.html": "/scorecard-thank-you/",
}


def clean_article(path: str) -> str:
    if path.startswith("insights/") and path.endswith(".html"):
        slug = path.removesuffix(".html")
        return "/" + slug + "/"
    return path


def normalize_url(url: str) -> str:
    if not url or url.startswith(("#", "/", "http://", "https://", "mailto:", "tel:", "data:")):
        return url
    base, anchor = (url.split("#", 1) + [""])[:2] if "#" in url else (url, "")
    query = ""
    if "?" in base:
        base, query = base.split("?", 1)
        query = "?" + query
    normalized = PAGE_MAP.get(base, clean_article(base))
    if normalized.startswith("assets/"):
        normalized = "/" + normalized
    if normalized in {"home.css", "home.js", "favicon.ico", "favicon.png", "apple-touch-icon.png", "social-preview.png"}:
        normalized = "/" + normalized
    return normalized + query + (("#" + anchor) if anchor else "")


def repl(match):
    attr, quote, url = match.groups()
    return f'{attr}={quote}{normalize_url(url)}{quote}'


for page in ROOT.rglob("*.html"):
    if ".git" in page.parts:
        continue
    text = page.read_text(encoding="utf-8")
    text = re.sub(r'\b(href|src|action)=(["\'])([^"\']+)\2', repl, text)
    page.write_text(text, encoding="utf-8", newline="\n")

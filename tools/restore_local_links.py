from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

ROOT_PAGE_MAP = {
    "/": "index.html",
    "/how-we-help/": "how-we-help.html",
    "/our-offerings/": "our-offerings.html",
    "/free-fit-check/": "free-fit-check.html",
    "/dashboard-trust-scorecard/": "dashboard-trust-scorecard.html",
    "/dashboard-trust-scorecard-download/": "dashboard-trust-scorecard-download.html",
    "/scorecard-thank-you/": "scorecard-thank-you.html",
    "/analytics-health-check/": "analytics-health-check.html",
    "/decision-system-reset/": "decision-system-reset.html",
    "/fractional-analytics/": "fractional-analytics.html",
    "/intelligence-lab/": "intelligence-lab.html",
    "/insights/": "insights.html",
    "/about/": "about.html",
    "/privacy-policy/": "privacy-policy.html",
    "/thank-you/": "thank-you.html",
    "/404.html": "404.html",
}


def page_prefix(page: Path) -> str:
    parent = page.relative_to(ROOT).parent
    if parent == Path("."):
        return ""
    return "../" * len(parent.parts)


def target_for(root_href: str) -> str | None:
    if root_href in ROOT_PAGE_MAP:
        return ROOT_PAGE_MAP[root_href]
    if root_href.startswith("/insights/") and root_href.endswith("/"):
        return root_href.lstrip("/").rstrip("/") + ".html"
    return None


def convert_href(href: str, prefix: str) -> str:
    if not href.startswith("/") or href.startswith("//"):
        return href
    path, anchor = (href.split("#", 1) + [""])[:2] if "#" in href else (href, "")
    target = target_for(path)
    if not target:
        return href
    return prefix + target + (("#" + anchor) if anchor else "")


def convert_asset(value: str, prefix: str) -> str:
    if value.startswith("/assets/"):
        return prefix + value.lstrip("/")
    if value in {"/home.css", "/home.js", "/favicon.ico", "/favicon.png", "/apple-touch-icon.png", "/social-preview.png"}:
        return prefix + value.lstrip("/")
    if value.startswith("/home.css?"):
        return prefix + value.lstrip("/")
    if value.startswith("/home.js?"):
        return prefix + value.lstrip("/")
    return value


def replace_attrs(text: str, prefix: str) -> str:
    def repl(match: re.Match) -> str:
        attr, quote, value = match.groups()
        if attr == "href":
            value = convert_href(value, prefix)
            value = convert_asset(value, prefix)
        elif attr == "src":
            value = convert_asset(value, prefix)
        return f'{attr}={quote}{value}{quote}'

    return re.sub(r'\b(href|src)=(["\'])([^"\']+)\2', repl, text)


for page in ROOT.rglob("*.html"):
    if ".git" in page.parts:
        continue
    prefix = page_prefix(page)
    text = page.read_text(encoding="utf-8")
    text = replace_attrs(text, prefix)
    page.write_text(text, encoding="utf-8", newline="\n")

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    "about",
    "analytics-health-check",
    "business-intelligence-consultant-cincinnati",
    "case-studies",
    "contact",
    "dashboard-trust-scorecard",
    "dashboard-trust-scorecard-download",
    "data-quality-review",
    "data-integration-analytics-architecture",
    "decision-system-reset",
    "expertise",
    "fractional-analytics",
    "how-we-help",
    "dashboard-trust-governance",
    "insights",
    "intelligence-lab",
    "kpi-reporting-consulting",
    "our-offerings",
    "power-bi-consultant-cincinnati",
    "reporting-automation-consulting",
]


def prefix_nested_paths(html: str) -> str:
    html = re.sub(r'(href|src)="(assets/[^"]*)"', r'\1="../\2"', html)
    html = re.sub(r'(href|src)="(home(?:\.min)?\.(?:css|js)\?v=\d+)"', r'\1="../\2"', html)
    html = re.sub(r'(href)="((?:favicon|apple-touch-icon|social-preview)[^"]*)"', r'\1="../\2"', html)
    html = re.sub(r"url\('assets/", "url('../assets/", html)

    def local_href(match: re.Match) -> str:
        target = match.group(1)
        if target.startswith(("#", "/", "../", "assets/", "http://", "https://", "mailto:", "tel:")):
            return f'href="{target}"'
        if ".html" in target or target.startswith("insights/"):
            return f'href="../{target}"'
        return f'href="{target}"'

    return re.sub(r'href="([^"]+)"', local_href, html)


def main() -> None:
    changed = []
    for slug in PAGES:
        source = ROOT / f"{slug}.html"
        target = ROOT / slug / "index.html"
        if not source.exists() or not target.parent.exists():
            continue
        target.write_text(prefix_nested_paths(source.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
        changed.append(target.relative_to(ROOT).as_posix())
    print("\n".join(changed))


if __name__ == "__main__":
    main()

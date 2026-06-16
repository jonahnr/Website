from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
SOCIAL_URLS = [
    "https://www.linkedin.com/company/129543938/admin/dashboard/",
    "https://www.youtube.com/@ParallaxDataLab",
    "https://www.instagram.com/parallaxdatalab/",
    "https://x.com/parallaxdatalab",
]


SOCIAL_GROUP = """<div class="site-footer-social" aria-label="Parallax Data Lab social profiles">
        <a class="site-social-link site-social-linkedin" href="https://www.linkedin.com/company/129543938/admin/dashboard/" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on LinkedIn"><span aria-hidden="true">in</span></a>
        <a class="site-social-link site-social-youtube" href="https://www.youtube.com/@ParallaxDataLab" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on YouTube"><span aria-hidden="true">YT</span></a>
        <a class="site-social-link site-social-instagram" href="https://www.instagram.com/parallaxdatalab/" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on Instagram"><span aria-hidden="true">IG</span></a>
        <a class="site-social-link site-social-x" href="https://x.com/parallaxdatalab" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on X"><span aria-hidden="true">X</span></a>
      </div>"""


class HeadParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title_parts: list[str] = []
        self.canonical = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: value or "" for key, value in attrs}
        if tag == "title":
            self.in_title = True
        elif tag == "link" and attr_map.get("rel") == "canonical":
            self.canonical = attr_map.get("href", "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self) -> str:
        return " ".join(" ".join(self.title_parts).split())


def update_footer(text: str) -> str:
    linkedin = re.compile(
        r'\s*<a class="site-footer-secondary" href="https://www\.linkedin\.com/company/129543938/admin/dashboard/" target="_blank" rel="noopener noreferrer">LinkedIn</a>'
    )
    if "site-footer-social" in text:
        return text
    return linkedin.sub("\n      " + SOCIAL_GROUP, text)


def update_home_tags(text: str) -> str:
    replacements = {
        "<span>Power BI dashboards</span>": "<span>Power BI Dashboards</span>",
        "<span>KPI reporting</span>": "<span>KPI Reporting</span>",
        "<span>analytics cleanup</span>": "<span>Analytics Cleanup</span>",
        "<span>reporting automation</span>": "<span>Reporting Automation</span>",
        "<span>data quality review</span>": "<span>Data Quality Review</span>",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def add_same_as_to_jsonld(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        body = match.group(1)
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return match.group(0)
        changed = False
        objects = data if isinstance(data, list) else [data]
        for obj in objects:
            if not isinstance(obj, dict):
                continue
            if obj.get("@type") in {"Organization", "ProfessionalService", "LocalBusiness"}:
                obj["sameAs"] = SOCIAL_URLS
                changed = True
            for key in ("author", "publisher"):
                nested = obj.get(key)
                if isinstance(nested, dict) and nested.get("@type") == "Organization":
                    nested["sameAs"] = SOCIAL_URLS
                    changed = True
        if not changed:
            return match.group(0)
        dumped = json.dumps(data, indent=2, ensure_ascii=False)
        return f'<script type="application/ld+json">{dumped}</script>'

    return re.sub(
        r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
        repl,
        text,
        flags=re.S,
    )


def add_article_share_block(path: Path, text: str) -> str:
    if "article-share" in text or '<article class="insight-article">' not in text:
        return text
    parser = HeadParser()
    parser.feed(text)
    if not parser.canonical:
        return text
    encoded_url = quote(parser.canonical, safe="")
    encoded_title = quote(parser.title, safe="")
    share = f"""<div class="article-share" aria-label="Share this article">
<strong>Share</strong>
<a href="https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
<a href="https://twitter.com/intent/tweet?url={encoded_url}&amp;text={encoded_title}" target="_blank" rel="noopener noreferrer">X</a>
</div>"""
    return text.replace('<nav aria-label="Related articles">', share + '\n<nav aria-label="Related articles">', 1)


def main() -> None:
    changed = []
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        new = update_footer(text)
        if path.name == "index.html" and path.parent == ROOT:
            new = update_home_tags(new)
        new = add_same_as_to_jsonld(new)
        new = add_article_share_block(path, new)
        if new != text:
            path.write_text(new, encoding="utf-8", newline="\n")
            changed.append(path.relative_to(ROOT).as_posix())
    print("changed_count=", len(changed))
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()

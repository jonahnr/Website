from pathlib import Path
from urllib.parse import quote
import re


ROOT = Path(__file__).resolve().parents[1]
X_HREF_RE = re.compile(r'href="https://x\.com/intent/(?:tweet|post)\?[^"]*"')


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text or "")).strip()


def page_title(html: str) -> str:
    meta = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', html)
    if meta:
        return meta.group(1).replace("&amp;", "&")
    title = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    return clean(title.group(1)).replace("&amp;", "&") if title else "Parallax Data Lab"


def canonical_url(html: str) -> str:
    canonical = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', html, re.I)
    if canonical:
        return canonical.group(1)
    og_url = re.search(r'<meta[^>]+property="og:url"[^>]+content="([^"]+)"', html)
    return og_url.group(1) if og_url else "https://parallaxdatalab.com/"


def update(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    if "x.com/intent/" not in html:
        return False
    share_text = f"{page_title(html)} {canonical_url(html)}"
    href = f'href="https://x.com/intent/post?text={quote(share_text, safe="")}"'
    updated = X_HREF_RE.sub(href, html)
    if updated == html:
        return False
    path.write_text(updated, encoding="utf-8", newline="")
    return True


def main():
    changed = []
    for path in list(ROOT.glob("*.html")) + list(ROOT.glob("*/*.html")) + list(ROOT.glob("insights/*/index.html")):
        if update(path):
            changed.append(path.relative_to(ROOT).as_posix())
    print(f"Rebuilt X share links in {len(changed)} files.")


if __name__ == "__main__":
    main()

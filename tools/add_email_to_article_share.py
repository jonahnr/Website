from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def title_and_url(html: str) -> tuple[str, str]:
    title_match = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', html)
    url_match = re.search(r'<meta[^>]+property="og:url"[^>]+content="([^"]+)"', html)
    title = title_match.group(1).replace("&amp;", "&") if title_match else "Parallax Data Lab article"
    url = url_match.group(1) if url_match else "https://parallaxdatalab.com/insights/"
    return title, url


def update(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    if '<div class="article-share"' not in html or "mailto:?subject=" in html:
        return False
    title, url = title_and_url(html)
    email = f'<a href="mailto:?subject={title}&amp;body={url}">Email</a>'
    updated = html.replace("</div>\n<nav aria-label=\"Related articles\">", f"{email}\n</div>\n<nav aria-label=\"Related articles\">", 1)
    if updated == html:
        return False
    path.write_text(updated, encoding="utf-8", newline="")
    return True


def main():
    changed = []
    for path in list((ROOT / "insights").glob("*.html")) + list((ROOT / "insights").glob("*/index.html")):
        if update(path):
            changed.append(path.relative_to(ROOT).as_posix())
    print(f"Added article email share links to {len(changed)} files.")


if __name__ == "__main__":
    main()

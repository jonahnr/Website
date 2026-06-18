from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def update(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    if '<article class="insight-article">' not in html:
      return False
    original = html
    date_match = re.search(r'<div class="article-meta"><span>Written by Jonah Robinson</span>\\s*<span>Published ([0-9-]+)</span></div>', html)
    if not date_match:
        return False
    date = date_match.group(1)
    html = re.sub(
        r'"author": \{\s*"@type": "Organization",\s*"name": "Parallax Data Lab",\s*"sameAs": \[[^\]]*\]\s*\}',
        '"author": {\n    "@type": "Person",\n    "name": "Jonah Robinson"\n  }',
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(r'"datePublished": "[^"]+"', f'"datePublished": "{date}"', html, count=1)
    if html != original:
        path.write_text(html, encoding="utf-8", newline="")
        return True
    return False


def main():
    changed = []
    for path in list((ROOT / "insights").glob("*.html")) + list((ROOT / "insights").glob("*/index.html")):
        if update(path):
            changed.append(path.relative_to(ROOT).as_posix())
    print(f"Updated article schema in {len(changed)} files.")


if __name__ == "__main__":
    main()

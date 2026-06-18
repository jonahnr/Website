from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
ARTICLE_FILES = [
    path
    for path in ROOT.glob("insights/**/*.html")
    if path.name != "index.html" or path.parent.name != "insights"
]

SHARE_PANEL_RE = re.compile(
    r'\n<section class="share-link-panel share-link-compact" aria-label="Share this page">.*?</section>\n',
    re.DOTALL,
)


def repair_file(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    if '<article class="insight-article">' not in html:
        return False

    updated = SHARE_PANEL_RE.sub("\n", html)
    if updated == html:
        return False

    path.write_text(updated, encoding="utf-8", newline="")
    return True


def main() -> None:
    changed = [path for path in ARTICLE_FILES if repair_file(path)]
    print(f"Removed duplicate in-article share panels from {len(changed)} article files.")
    for path in changed:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()

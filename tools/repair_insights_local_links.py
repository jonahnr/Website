from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
INSIGHTS = ROOT / "insights"

ARTICLE_SLUGS = sorted(
    path.name for path in INSIGHTS.iterdir()
    if path.is_dir() and (path / "index.html").exists()
)


def write_if_changed(path: Path, text: str) -> bool:
    old = path.read_text(encoding="utf-8")
    if old == text:
        return False
    path.write_text(text, encoding="utf-8", newline="")
    return True


def repair_root_hub() -> bool:
    path = ROOT / "insights.html"
    text = path.read_text(encoding="utf-8")
    for slug in ARTICLE_SLUGS:
        text = text.replace(f'href="insights/{slug}/"', f'href="insights/{slug}.html"')
    return write_if_changed(path, text)


def repair_nested_hub() -> bool:
    path = INSIGHTS / "index.html"
    text = path.read_text(encoding="utf-8")
    for slug in ARTICLE_SLUGS:
        text = text.replace(f'href="{slug}/"', f'href="{slug}/index.html"')
    return write_if_changed(path, text)


def repair_nested_articles() -> int:
    changed = 0
    for index_path in INSIGHTS.glob("*/index.html"):
        text = index_path.read_text(encoding="utf-8")
        text = text.replace('href="../"', 'href="../index.html"')
        for slug in ARTICLE_SLUGS:
            text = text.replace(f'href="../{slug}/"', f'href="../{slug}/index.html"')
        if write_if_changed(index_path, text):
            changed += 1
    return changed


def main() -> None:
    changed = []
    if repair_root_hub():
        changed.append("insights.html")
    if repair_nested_hub():
        changed.append("insights/index.html")
    nested_count = repair_nested_articles()
    print(f"Updated local-safe article links in {len(changed)} hub files and {nested_count} nested article files.")
    if changed:
        print("\n".join(changed))


if __name__ == "__main__":
    main()

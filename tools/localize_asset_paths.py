from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def depth_prefix(page: Path) -> str:
    rel_parent = page.relative_to(ROOT).parent
    if rel_parent == Path("."):
        return ""
    return "../" * len(rel_parent.parts)


def localize(page: Path) -> None:
    text = page.read_text(encoding="utf-8")
    prefix = depth_prefix(page)

    # Keep deployed clean URLs for page navigation, but make local assets
    # relative so file:// previews still render with CSS, JS, images, icons.
    asset_prefix = prefix
    replacements = {
        'href="/home.css': f'href="{asset_prefix}home.css',
        'src="/home.js': f'src="{asset_prefix}home.js',
        'href="/favicon.ico': f'href="{asset_prefix}favicon.ico',
        'href="/favicon.png': f'href="{asset_prefix}favicon.png',
        'href="/apple-touch-icon.png': f'href="{asset_prefix}apple-touch-icon.png',
        'src="/assets/': f'src="{asset_prefix}assets/',
    }
    for before, after in replacements.items():
        text = text.replace(before, after)

    page.write_text(text, encoding="utf-8", newline="\n")


for html in ROOT.rglob("*.html"):
    if ".git" in html.parts:
        continue
    localize(html)

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strip_webp_srcsets(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        srcset_match = re.search(r'\s+srcset=(["\'])(.*?)\1', tag, flags=re.I | re.S)
        if not srcset_match or ".webp" not in srcset_match.group(2).lower():
            return tag
        tag = re.sub(r'\s+srcset=(["\']).*?\1', "", tag, flags=re.I | re.S)
        tag = re.sub(r'\s+sizes=(["\']).*?\1', "", tag, flags=re.I | re.S)
        return tag

    return re.sub(r"<img\b[^>]*>", repl, text, flags=re.I | re.S)


def replace_image_set(text: str) -> str:
    pattern = re.compile(
        r'image-set\(\s*url\((["\'])([^"\']+\.webp)\1\)\s+type\(["\']image/webp["\']\)\s*,\s*'
        r'url\((["\'])([^"\']+\.(?:png|jpg|jpeg))\3\)\s+type\(["\']image/(?:png|jpeg|jpg)["\']\)\s*\)',
        flags=re.I,
    )
    return pattern.sub(lambda m: f'url("{m.group(4)}")', text)


def main() -> None:
    changed = []
    for path in list(ROOT.rglob("*.html")) + list(ROOT.rglob("*.css")) + list(ROOT.rglob("*.js")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        new = text
        if path.suffix.lower() == ".html":
            new = strip_webp_srcsets(new)
        new = replace_image_set(new)
        new = new.replace("assets/social-preview.jpg", "assets/social-preview.png")
        if new != text:
            path.write_text(new, encoding="utf-8", newline="\n")
            changed.append(path.relative_to(ROOT).as_posix())
    print("changed_count=", len(changed))
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()

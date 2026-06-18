from __future__ import annotations

import re
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://parallaxdatalab.com"
EXCLUDE_SHARE = {
    "privacy-policy.html",
    "scorecard-thank-you.html",
    "dashboard-trust-scorecard-download.html",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def page_url(path: Path, text: str) -> str:
    canon = re.search(r'<link rel="canonical" href="([^"]+)"/?>', text)
    if canon:
        return canon.group(1)
    if path.name == "index.html":
        return f"{SITE}/"
    return f"{SITE}/{path.with_suffix('').as_posix()}/"


def page_title(text: str) -> str:
    og = re.search(r'<meta property="og:title" content="([^"]+)"/>', text)
    if og:
        return og.group(1).replace(" | Parallax Data Lab", "")
    title = re.search(r"<title>(.*?)</title>", text, re.S)
    return (title.group(1).replace(" | Parallax Data Lab", "") if title else "Parallax Data Lab").strip()


def share_markup(url: str, title: str) -> str:
    safe_url = escape(url, quote=True)
    safe_title = escape(title, quote=True)
    linkedin = f"https://www.linkedin.com/sharing/share-offsite/?url={safe_url}"
    x_url = f"https://x.com/intent/tweet?url={safe_url}&text={safe_title}"
    mail = f"mailto:?subject={safe_title}&body={safe_url}"
    return f'''<section class="share-link-panel share-link-compact" aria-label="Share this page">
<span class="share-link-label">Share</span>
<button type="button" data-native-share="{safe_url}" data-share-title="{safe_title}">Share Link</button>
<button type="button" data-copy-share="{safe_url}">Copy</button>
<a class="share-link-social" href="{linkedin}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
<a class="share-link-social" href="{x_url}" target="_blank" rel="noopener noreferrer">X</a>
<a class="share-link-social" href="{mail}">Email</a>
</section>'''


def replace_or_insert_share(path: Path, text: str) -> str:
    if path.name in EXCLUDE_SHARE or "<main" not in text:
        return text
    url = page_url(path, text)
    title = page_title(text)
    markup = share_markup(url, title)
    pattern = re.compile(r'<section class="share-link-panel[^"]*" aria-label="Share this page">.*?</section>', re.S)
    if pattern.search(text):
        return pattern.sub(markup, text, count=1)
    main_match = re.search(r"<main\b[^>]*>.*?</section>", text, re.S)
    if not main_match:
        return text
    insert_at = main_match.end()
    return text[:insert_at] + "\n" + markup + text[insert_at:]


def mailto_footers(text: str) -> str:
    return re.sub(
        r'<a class="site-footer-email" href="#" data-mail-user="jonahnr" data-mail-domain="gmail.com" data-mail-subject="Parallax Data Lab Inquiry">Email us</a>',
        '<a class="site-footer-email" href="mailto:jonahnr@gmail.com?subject=Parallax%20Data%20Lab%20Inquiry">Email us</a>',
        text,
    )


def insight_backgrounds() -> dict[str, str]:
    mapping = {}
    for article in (ROOT / "insights").glob("*.html"):
        text = read(article)
        img = re.search(r'"image"\s*:\s*"https://parallaxdatalab.com/([^"]+)"', text)
        if not img:
            img = re.search(r'<meta[^>]+property="og:image"[^>]+content="https://parallaxdatalab.com/([^"]+)"', text)
        if not img:
            img = re.search(r'<meta[^>]+content="https://parallaxdatalab.com/([^"]+)"[^>]+property="og:image"', text)
        if img:
            mapping[f"insights/{article.name}"] = img.group(1)
    return mapping


def add_related_backgrounds(text: str, backgrounds: dict[str, str]) -> str:
    def repl(match: re.Match) -> str:
        tag = match.group(0)
        href = match.group(1)
        if href not in backgrounds:
            return tag
        if "style=" in tag:
            return re.sub(r'style="[^"]*"', f'style="--article-bg: url(\'{backgrounds[href]}\')"', tag)
        return tag.replace('class="expertise-article-card"', f'class="expertise-article-card" style="--article-bg: url(\'{backgrounds[href]}\')"')
    return re.sub(r'<a class="expertise-article-card"(?: style="[^"]*")? href="([^"]+)">', repl, text)


def move_reset_deliverables(text: str) -> str:
    cta_pattern = re.compile(r'<section aria-labelledby="reset-cta-title" class="reset-cta-refined reveal-card">.*?</section>', re.S)
    deliverable_pattern = re.compile(r'<section class="deliverable-proof-section reveal-card" aria-labelledby="decision-system-reset-deliverables-title">.*?</section>', re.S)
    cta = cta_pattern.search(text)
    deliverable = deliverable_pattern.search(text)
    if not cta or not deliverable or deliverable.start() < cta.start():
        return text
    deliverable_html = deliverable.group(0)
    text = text[:deliverable.start()] + text[deliverable.end():]
    cta = cta_pattern.search(text)
    if not cta:
        return text + "\n" + deliverable_html
    return text[:cta.start()] + deliverable_html + "\n" + text[cta.start():]


def main() -> None:
    backgrounds = insight_backgrounds()
    changed = []
    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts:
            continue
        original = read(path)
        text = original
        text = mailto_footers(text)
        text = replace_or_insert_share(path, text)
        text = add_related_backgrounds(text, backgrounds)
        if path.name == "decision-system-reset.html" or path.parent.name == "decision-system-reset":
            text = move_reset_deliverables(text)
        if text != original:
            write(path, text)
            changed.append(path.relative_to(ROOT).as_posix())
    print(f"updated_html={len(changed)}")
    for item in changed[:80]:
        print(item)


if __name__ == "__main__":
    main()

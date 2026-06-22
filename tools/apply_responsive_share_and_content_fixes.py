from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def page_url_from_path(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "https://parallaxdatalab.com/"
    if rel.endswith("/index.html"):
        clean = rel[: -len("index.html")]
        return f"https://parallaxdatalab.com/{clean}"
    if rel.endswith(".html"):
        stem = rel[:-5]
        if stem == "404":
            return "https://parallaxdatalab.com/404.html"
        return f"https://parallaxdatalab.com/{stem}/"
    return "https://parallaxdatalab.com/"


def page_title(text: str) -> str:
    match = re.search(r"<title>(.*?)</title>", text, flags=re.I | re.S)
    if match:
        return re.sub(r"\s+", " ", match.group(1)).strip()
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", text, flags=re.I | re.S)
    if h1:
        return re.sub(r"<[^>]+>", "", h1.group(1)).strip()
    return "Parallax Data Lab"


def share_panel(url: str, title: str) -> str:
    mail_subject = quote(title, safe="")
    x_text = quote(f"{title} {url}", safe="")
    return (
        '<section class="share-link-panel share-link-compact" aria-label="Share this page">\n'
        '<span class="share-link-label">Share</span>\n'
        f'<a class="share-link-social" href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener noreferrer" aria-label="Share on LinkedIn"></a>\n'
        f'<a class="share-link-social" href="https://x.com/intent/post?text={x_text}" target="_blank" rel="noopener noreferrer" aria-label="Share on X"></a>\n'
        f'<a class="share-link-social" href="mailto:?subject={mail_subject}&amp;body={quote(url, safe=":/")}" aria-label="Share by email"></a>\n'
        f'<button class="share-link-social share-native-button" type="button" data-native-share="{url}" aria-label="Share this page"></button>\n'
        "</section>"
    )


def article_share(url: str, title: str) -> str:
    mail_subject = quote(title, safe="")
    x_text = quote(f"{title} {url}", safe="")
    return (
        '<div class="article-share" aria-label="Share this article">\n'
        "<strong>Share</strong>\n"
        f'<a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener noreferrer" aria-label="Share on LinkedIn"></a>\n'
        f'<a href="https://x.com/intent/post?text={x_text}" target="_blank" rel="noopener noreferrer" aria-label="Share on X"></a>\n'
        f'<a href="mailto:?subject={mail_subject}&amp;body={quote(url, safe=":/")}" aria-label="Share by email"></a>\n'
        f'<button class="share-link-social share-native-button" type="button" data-native-share="{url}" aria-label="Share this article"></button>\n'
        "</div>"
    )


def normalize_share_blocks() -> None:
    for path in ROOT.rglob("*.html"):
        if any(part in {".git", "node_modules"} for part in path.parts):
            continue
        text = read(path)
        title = page_title(text)
        url = page_url_from_path(path)
        new = re.sub(
            r'<section class="share-link-panel share-link-compact" aria-label="Share this page">.*?</section>',
            lambda _: share_panel(url, title),
            text,
            flags=re.S,
        )
        new = re.sub(
            r'<div class="article-share" aria-label="Share this article">.*?</div>',
            lambda _: article_share(url, title),
            new,
            flags=re.S,
        )
        if new != text:
            write(path, new)


def move_section_after_share(path: Path, section_class: str) -> None:
    text = read(path)
    section_match = re.search(
        rf'\n<section class="{re.escape(section_class)} reveal-card".*?</section>',
        text,
        flags=re.S,
    )
    share_match = re.search(
        r'\n<section class="share-link-panel share-link-compact" aria-label="Share this page">.*?</section>',
        text,
        flags=re.S,
    )
    if not section_match or not share_match or section_match.start() > share_match.start():
        return
    section = section_match.group(0)
    without = text[: section_match.start()] + text[section_match.end() :]
    share_match = re.search(
        r'\n<section class="share-link-panel share-link-compact" aria-label="Share this page">.*?</section>',
        without,
        flags=re.S,
    )
    if not share_match:
        return
    new = without[: share_match.end()] + section + without[share_match.end() :]
    write(path, new)


def content_fixes() -> None:
    for rel in ["index.html", "about.html", "about/index.html"]:
        path = ROOT / rel
        if not path.exists():
            continue
        text = read(path)
        text = text.replace("<strong>5+ years</strong>", "<strong>7+ years</strong>")
        text = text.replace(
            "<span>delivering enterprise analytics solutions</span>",
            "<span>delivering enterprise analytics solutions across manufacturing, healthcare, safety, operations, and SaaS</span>",
        )
        text = text.replace(
            "<span>of records supported across modern cloud analytics environments</span>",
            "<span>supported across modern cloud analytics environments</span>",
        )
        text = text.replace(
            "<strong>Millions to billions</strong><span>supported across modern cloud analytics environments</span>",
            "<strong>2 billion records +</strong><span>supported across modern cloud analytics environments</span>",
        )
        text = text.replace(
            "<strong>Millions to billions</strong><span>of records supported across modern cloud analytics environments</span>",
            "<strong>2 billion records +</strong><span>supported across modern cloud analytics environments</span>",
        )
        write(path, text)

    index = ROOT / "index.html"
    text = read(index)
    text = text.replace(' <span aria-hidden="true">-&gt;</span>', "")
    write(index, text)

    for rel in [
        "business-intelligence-consultant-cincinnati.html",
        "business-intelligence-consultant-cincinnati/index.html",
    ]:
        path = ROOT / rel
        if not path.exists():
            continue
        text = read(path)
        text = text.replace(
            "<p>These company names describe the regional business landscape only; they are not presented as Parallax Data Lab clients, employers, or project references.</p>\n",
            "",
        )
        write(path, text)

    for rel in ["kpi-reporting-consulting.html", "kpi-reporting-consulting/index.html"]:
        move_section_after_share(ROOT / rel, "expertise-strategy-section")

    for rel in [
        "reporting-automation-consulting.html",
        "reporting-automation-consulting/index.html",
    ]:
        move_section_after_share(ROOT / rel, "expertise-strategy-section")


if __name__ == "__main__":
    normalize_share_blocks()
    content_fixes()

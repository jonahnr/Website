from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
ARTICLE_DATES = [
    "2026-03-12", "2026-03-18", "2026-03-25", "2026-04-02", "2026-04-09",
    "2026-04-15", "2026-04-22", "2026-04-29", "2026-05-05", "2026-05-08",
    "2026-05-13", "2026-05-16", "2026-05-20", "2026-05-23", "2026-05-28",
    "2026-06-02", "2026-06-04", "2026-06-06", "2026-06-08", "2026-06-10",
    "2026-06-11", "2026-06-12", "2026-06-13", "2026-06-14", "2026-06-15",
    "2026-06-16",
]


def page_files():
    yield from ROOT.glob("*.html")
    yield from ROOT.glob("*/*.html")
    yield from ROOT.glob("insights/*/index.html")


def update_footer_email(html: str) -> str:
    email = '<a class="site-footer-email" href="mailto:jonahnr@gmail.com?subject=Parallax%20Data%20Lab%20Inquiry">Email us</a>'
    html = html.replace(f"\n      {email}", "")
    if "site-footer-contact" in html and email not in html:
        html = html.replace(
            '<a class="site-footer-secondary" href="about.html#contact-us">Contact Parallax Data Lab</a>',
            '<a class="site-footer-secondary" href="about.html#contact-us">Contact Parallax Data Lab</a>\n      <a class="site-footer-email site-footer-contact-email" href="mailto:jonahnr@gmail.com?subject=Parallax%20Data%20Lab%20Inquiry">Email us</a>'
        )
        html = html.replace(
            '<a class="site-footer-secondary" href="../about.html#contact-us">Contact Parallax Data Lab</a>',
            '<a class="site-footer-secondary" href="../about.html#contact-us">Contact Parallax Data Lab</a>\n      <a class="site-footer-email site-footer-contact-email" href="mailto:jonahnr@gmail.com?subject=Parallax%20Data%20Lab%20Inquiry">Email us</a>'
        )
        html = html.replace(
            '<a class="site-footer-secondary" href="../../about.html#contact-us">Contact Parallax Data Lab</a>',
            '<a class="site-footer-secondary" href="../../about.html#contact-us">Contact Parallax Data Lab</a>\n      <a class="site-footer-email site-footer-contact-email" href="mailto:jonahnr@gmail.com?subject=Parallax%20Data%20Lab%20Inquiry">Email us</a>'
        )
    return html


def update_scorecard_form(html: str) -> str:
    html = html.replace('action="https://formsubmit.co/"', 'action="/api/scorecard-submit"')
    html = html.replace('data-scorecard-delivery="formsubmit"', 'data-scorecard-delivery="backend"')
    html = html.replace(
        "Submissions are emailed through FormSubmit on the hosted site. A browser-side CSV backup is also stored after submit so you can download a local archive from the scorecard page if needed.",
        ""
    )
    return html


def update_share_urls(html: str) -> str:
    html = html.replace("https://twitter.com/intent/tweet", "https://x.com/intent/post")
    return html


def update_versions(html: str) -> str:
    html = re.sub(r"home\.css\?v=\d+", "home.css?v=138", html)
    html = re.sub(r"home\.js\?v=\d+", "home.js?v=138", html)
    return html


def update_article_meta(path: Path, html: str, index: int) -> str:
    if '<article class="insight-article">' not in html:
        return html
    date = ARTICLE_DATES[index % len(ARTICLE_DATES)]
    new_meta = f'<div class="article-meta"><span>Written by Jonah Robinson</span> <span>Published {date}</span></div>'
    html = re.sub(r'<div class="article-meta">.*?</div>', new_meta, html, count=1, flags=re.S)
    return html


def main():
    changed = []
    article_counter = 0
    for path in page_files():
        html = path.read_text(encoding="utf-8")
        original = html
        html = update_footer_email(html)
        html = update_scorecard_form(html)
        html = update_share_urls(html)
        html = update_versions(html)
        if '<article class="insight-article">' in html:
            html = update_article_meta(path, html, article_counter)
            article_counter += 1
        if html != original:
            path.write_text(html, encoding="utf-8", newline="")
            changed.append(path.relative_to(ROOT).as_posix())
    print(f"Updated {len(changed)} files; article metadata updated on {article_counter} article files.")
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
USER = "jonahnr"
DOMAIN = "gmail.com"

LINKEDIN_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5.1 8.4h3.8v11.5H5.1V8.4Zm1.9-5.7a2.2 2.2 0 1 1 0 4.4 2.2 2.2 0 0 1 0-4.4Zm4.1 5.7h3.6v1.6h.1c.5-.9 1.7-1.9 3.5-1.9 3.7 0 4.4 2.4 4.4 5.6v6.2h-3.8v-5.5c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9v5.6h-3.8V8.4Z"/></svg>'
YOUTUBE_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 7.1a3 3 0 0 0-2.1-2.1C18 4.5 12 4.5 12 4.5s-6 0-7.9.5A3 3 0 0 0 2 7.1 31.6 31.6 0 0 0 1.5 12c0 1.7.2 3.4.5 4.9A3 3 0 0 0 4.1 19c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1c.3-1.5.5-3.2.5-4.9s-.2-3.4-.5-4.9ZM10 15.2V8.8l5.6 3.2-5.6 3.2Z"/></svg>'
INSTAGRAM_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7.2 2.8h9.6a4.4 4.4 0 0 1 4.4 4.4v9.6a4.4 4.4 0 0 1-4.4 4.4H7.2a4.4 4.4 0 0 1-4.4-4.4V7.2a4.4 4.4 0 0 1 4.4-4.4Zm0 2A2.4 2.4 0 0 0 4.8 7.2v9.6a2.4 2.4 0 0 0 2.4 2.4h9.6a2.4 2.4 0 0 0 2.4-2.4V7.2a2.4 2.4 0 0 0-2.4-2.4H7.2Zm4.8 3a4.2 4.2 0 1 1 0 8.4 4.2 4.2 0 0 1 0-8.4Zm0 2a2.2 2.2 0 1 0 0 4.4 2.2 2.2 0 0 0 0-4.4Zm4.6-2.9a1 1 0 1 1 0 2.1 1 1 0 0 1 0-2.1Z"/></svg>'
X_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.8 10.4 21.1 2h-1.7l-6.3 7.2L8 2H2.2l7.7 11-7.7 9h1.7l6.8-7.8 5.5 7.8H22l-8.2-11.6Zm-2.4 2.8-.8-1.1L4.4 3.3h2.8l5 7.1.8 1.1 6.5 9.2h-2.8l-5.3-7.5Z"/></svg>'

SOCIAL_GROUP = f"""<div class="site-footer-social" aria-label="Parallax Data Lab social profiles">
        <a class="site-social-link site-social-linkedin" href="https://www.linkedin.com/company/129543938/admin/dashboard/" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on LinkedIn">{LINKEDIN_ICON}</a>
        <a class="site-social-link site-social-youtube" href="https://www.youtube.com/@ParallaxDataLab" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on YouTube">{YOUTUBE_ICON}</a>
        <a class="site-social-link site-social-instagram" href="https://www.instagram.com/parallaxdatalab/" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on Instagram">{INSTAGRAM_ICON}</a>
        <a class="site-social-link site-social-x" href="https://x.com/parallaxdatalab" target="_blank" rel="noopener noreferrer" aria-label="Parallax Data Lab on X">{X_ICON}</a>
      </div>"""

EMAIL_LINK = f'<a class="site-footer-email" href="#" data-mail-user="{USER}" data-mail-domain="{DOMAIN}" data-mail-subject="Parallax Data Lab Inquiry">Email us</a>'
ABOUT_EMAIL_LINK = f'<a class="about-email-link" href="#" data-mail-user="{USER}" data-mail-domain="{DOMAIN}" data-mail-subject="Parallax Data Lab Inquiry">Email us</a>'


def update_html(text: str) -> str:
    text = re.sub(r'\s+"email":\s*"[^"]+",?\n', "\n", text)
    text = re.sub(
        r'Contact Parallax Data Lab at [^ ]+ with privacy questions or requests related to information you submitted through this site\.',
        "Contact Parallax Data Lab with privacy questions or requests related to information you submitted through this site.",
        text,
    )
    text = re.sub(
        r'<a href="mailto:[^"]+">Email Jonah</a>',
        f'<a href="#" data-mail-user="{USER}" data-mail-domain="{DOMAIN}" data-mail-subject="Parallax Data Lab Privacy Question">Email us</a>',
        text,
    )
    text = re.sub(
        r'<a class="site-footer-email" href="mailto:[^"]+">[^<]+</a>',
        EMAIL_LINK,
        text,
    )
    text = re.sub(
        r'<a class="about-email-link" href="mailto:[^"]+">[^<]+</a>',
        ABOUT_EMAIL_LINK,
        text,
    )
    text = re.sub(
        r'<form action="https://formsubmit\.co/[^"]+"',
        f'<form action="https://formsubmit.co/" data-form-user="{USER}" data-form-domain="{DOMAIN}"',
        text,
    )
    text = re.sub(
        r'\sdata-local-mail-fallback="[^"]+"',
        "",
        text,
    )
    text = re.sub(
        r'<div class="site-footer-social" aria-label="Parallax Data Lab social profiles">.*?</div>',
        SOCIAL_GROUP,
        text,
        flags=re.S,
    )
    return text


def main() -> None:
    changed = []
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        new = update_html(text)
        if new != text:
            path.write_text(new, encoding="utf-8", newline="\n")
            changed.append(path.relative_to(ROOT).as_posix())
    print("changed_count=", len(changed))
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()

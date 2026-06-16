from html.parser import HTMLParser
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.srcsets = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            attrs = dict(attrs)
            if attrs.get("srcset"):
                self.srcsets.append(attrs["srcset"])


for html in ROOT.rglob("*.html"):
    if ".git" in html.parts:
        continue
    text = html.read_text(encoding="utf-8")
    # Logo should render immediately. Keep async decoding, but never lazy-load it.
    text = text.replace('alt="Parallax Data Lab logo" loading="lazy"', 'alt="Parallax Data Lab logo"')
    text = text.replace('loading="lazy" alt="Parallax Data Lab logo"', 'alt="Parallax Data Lab logo"')
    html.write_text(text, encoding="utf-8", newline="\n")


issues = []
for html in ROOT.rglob("*.html"):
    if ".git" in html.parts:
        continue
    parser = Parser()
    parser.feed(html.read_text(encoding="utf-8"))
    for srcset in parser.srcsets:
        for candidate in srcset.split(","):
            url = candidate.strip().split(" ", 1)[0]
            if not url or url.startswith(("http://", "https://", "data:", "/")):
                continue
            target = (html.parent / url.split("?", 1)[0]).resolve()
            if not str(target).lower().startswith(str(ROOT).lower()) or not target.exists():
                issues.append(f"{html.relative_to(ROOT).as_posix()}: missing srcset candidate {url}")

print(f"srcset_issue_count={len(issues)}")
for issue in issues[:100]:
    print("- " + issue)

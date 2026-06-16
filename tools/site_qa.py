from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.h1 = 0
        self.links = []
        self.images = []
        self.forms = []
        self.in_title = False
        self.title = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == "h1":
            self.h1 += 1
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "img":
            self.images.append((attrs.get("src", ""), attrs.get("alt")))
        if tag == "form":
            self.forms.append(attrs)
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def has_meta(parser, key, value):
    for tag, attrs in parser.tags:
        if tag == "meta" and attrs.get(key) == value:
            return True
    return False


def has_link_rel(parser, rel):
    return any(tag == "link" and attrs.get("rel") == rel for tag, attrs in parser.tags)


def local_target_exists(src, page):
    if not src or src.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return True
    path = src.split("#", 1)[0].split("?", 1)[0]
    if not path:
        return True
    if path.startswith("/"):
        target = ROOT / path.lstrip("/")
    else:
        target = page.parent / path
    return target.exists()


issues = []
titles = {}
descs = {}

for page in ROOT.rglob("*.html"):
    if ".git" in page.parts:
        continue
    parser = PageParser()
    text = page.read_text(encoding="utf-8")
    parser.feed(text)
    rel = page.relative_to(ROOT).as_posix()

    title = parser.title.strip()
    if not title:
        issues.append(f"{rel}: missing title")
    titles.setdefault(title, []).append(rel)

    desc = None
    for tag, attrs in parser.tags:
        if tag == "meta" and attrs.get("name") == "description":
            desc = attrs.get("content", "")
    if not desc:
        issues.append(f"{rel}: missing meta description")
    else:
        descs.setdefault(desc, []).append(rel)

    if parser.h1 != 1:
        issues.append(f"{rel}: expected 1 h1, found {parser.h1}")
    for required in ["og:title", "og:description", "og:url", "og:image"]:
        if not has_meta(parser, "property", required):
            issues.append(f"{rel}: missing {required}")
    for required in ["twitter:card", "twitter:title", "twitter:description", "twitter:image"]:
        if not has_meta(parser, "name", required):
            issues.append(f"{rel}: missing {required}")
    if not has_link_rel(parser, "canonical"):
        issues.append(f"{rel}: missing canonical")
    if "name=\"keywords\"" in text:
        issues.append(f"{rel}: still has meta keywords")
    for src, alt in parser.images:
        if alt is None:
            issues.append(f"{rel}: image missing alt: {src}")
        if not local_target_exists(src, page):
            issues.append(f"{rel}: missing image target: {src}")
    for href in parser.links:
        if not local_target_exists(href, page):
            issues.append(f"{rel}: missing link target: {href}")
    for form in parser.forms:
        if form.get("method", "").upper() != "POST":
            issues.append(f"{rel}: form method is not POST")
        if not form.get("action"):
            issues.append(f"{rel}: form missing action")

duplicate_titles = {k: v for k, v in titles.items() if k and len(v) > 1}
duplicate_descs = {k: v for k, v in descs.items() if k and len(v) > 1}

print("Issues:")
for issue in issues[:200]:
    print(f"- {issue}")
if len(issues) > 200:
    print(f"- ... {len(issues) - 200} more")

print(f"issue_count={len(issues)}")
print(f"duplicate_title_groups={len(duplicate_titles)}")
print(f"duplicate_description_groups={len(duplicate_descs)}")
for title, files in list(duplicate_titles.items())[:20]:
    print(f"duplicate_title: {title} -> {', '.join(files)}")

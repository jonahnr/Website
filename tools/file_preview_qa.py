from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for attr in ("href", "src"):
            value = attrs.get(attr)
            if value:
                self.refs.append((tag, attr, value))


def is_external(value: str) -> bool:
    return value.startswith(("#", "mailto:", "tel:", "http://", "https://", "data:", "//"))


def resolve(page: Path, value: str) -> Path | None:
    if is_external(value):
        return None
    path = value.split("#", 1)[0].split("?", 1)[0]
    if not path:
        return None
    if path.startswith("/"):
        return (ROOT / path.lstrip("/")).resolve()
    return (page.parent / unquote(path)).resolve()


issues = []
for page in ROOT.rglob("*.html"):
    if ".git" in page.parts:
        continue
    parser = Parser()
    parser.feed(page.read_text(encoding="utf-8"))
    for tag, attr, value in parser.refs:
        target = resolve(page, value)
        if target is None:
            continue
        if not str(target).lower().startswith(str(ROOT).lower()) or not target.exists():
            issues.append(f"{page.relative_to(ROOT).as_posix()}: {tag} {attr} unresolved in file preview -> {value}")

print("file_preview_issue_count=" + str(len(issues)))
for issue in issues[:200]:
    print("- " + issue)
if len(issues) > 200:
    print(f"- ... {len(issues) - 200} more")

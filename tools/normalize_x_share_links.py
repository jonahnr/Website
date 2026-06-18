from pathlib import Path
from urllib.parse import parse_qs, quote, unquote
import re


ROOT = Path(__file__).resolve().parents[1]


X_TWEET_RE = re.compile(r'https://x\.com/intent/tweet\?([^"\'<\s]+)')


def normalize(match: re.Match) -> str:
    query = match.group(1).replace("&amp;", "&")
    parsed = parse_qs(query, keep_blank_values=True)
    url = unquote(parsed.get("url", [""])[0])
    text = unquote(parsed.get("text", [""])[0])
    combined = " ".join(part for part in [text, url] if part).strip()
    return f"https://x.com/intent/post?text={quote(combined)}"


def update(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    updated = X_TWEET_RE.sub(normalize, text)
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8", newline="")
    return True


def main():
    changed = []
    for path in list(ROOT.glob("*.html")) + list(ROOT.glob("*/*.html")) + list(ROOT.glob("insights/*/index.html")):
        if update(path):
            changed.append(path.relative_to(ROOT).as_posix())
    print(f"Normalized X share links in {len(changed)} files.")


if __name__ == "__main__":
    main()

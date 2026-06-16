from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT / "our-offerings" / "index.html"]


def should_prefix(value: str) -> bool:
    if value.startswith(("#", "../", "./", "http://", "https://", "mailto:", "tel:", "data:", "//")):
        return False
    return True


for page in PAGES:
    text = page.read_text(encoding="utf-8")

    def repl(match: re.Match) -> str:
        attr, quote, value = match.groups()
        if should_prefix(value):
            value = "../" + value
        return f'{attr}={quote}{value}{quote}'

    text = re.sub(r'\b(href|src)=(["\'])([^"\']+)\2', repl, text)
    page.write_text(text, encoding="utf-8", newline="\n")

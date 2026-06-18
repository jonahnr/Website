from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

for html in ROOT.rglob("*.html"):
    if ".git" in html.parts:
        continue
    text = html.read_text(encoding="utf-8")

    def repl(match: re.Match) -> str:
        tag = match.group(0)
        if "Parallax Data Lab logo" in tag:
            tag = re.sub(r'\sloading=(["\'])lazy\1', "", tag)
        return tag

    text = re.sub(r"<img\b[^>]*>", repl, text)
    html.write_text(text, encoding="utf-8", newline="\n")

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

for html in ROOT.rglob("*.html"):
    if ".git" in html.parts:
        continue
    text = html.read_text(encoding="utf-8")
    # The image optimizer appended attributes to self-closing <img .../> tags,
    # creating invalid markup like: <img src="x.png"/ srcset="...">
    text = re.sub(r'(<img\b[^>]*?)\s*/\s+(srcset|sizes|loading|decoding)=', r'\1 \2=', text)
    text = re.sub(r'(<img\b[^>]*?)\s*/\s*>', r'\1>', text)
    html.write_text(text, encoding="utf-8", newline="\n")

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD = "https://parallaxdatalab.com/assets/social-preview.png"
OLD_ROOT = "https://parallaxdatalab.com/social-preview.png"
NEW = "https://parallaxdatalab.com/assets/social-preview.jpg"

for html in ROOT.rglob("*.html"):
    if ".git" in html.parts:
        continue
    text = html.read_text(encoding="utf-8")
    text = text.replace(OLD, NEW).replace(OLD_ROOT, NEW)
    html.write_text(text, encoding="utf-8", newline="\n")

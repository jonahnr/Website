from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sources = [
    (ROOT / "social-preview.png", ROOT / "social-preview.jpg"),
    (ROOT / "assets" / "social-preview.png", ROOT / "assets" / "social-preview.jpg"),
]

for src, dest in sources:
    if not src.exists():
        continue
    img = Image.open(src).convert("RGB")
    if img.size != (1200, 630):
        img = img.resize((1200, 630), Image.Resampling.LANCZOS)
    img.save(dest, "JPEG", quality=84, optimize=True, progressive=True)
    print(f"{dest.relative_to(ROOT).as_posix()} {dest.stat().st_size}")
